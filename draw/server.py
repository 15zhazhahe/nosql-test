from pandas import DataFrame
import pandas as pd
import numpy as np
from flask import Flask, render_template
from flask import request
from pymongo import MongoClient
from pyecharts import Line
from bson.code import Code

# 配置主题便于字体显示
# pyecharts.configure(global_theme='dark')

# 连接数据库
conn = MongoClient('localhost', 27017)
db = conn.mydb
my_set = db.test_set

REMOTE_HOST = "https://pyecharts.github.io/assets/js"
app = Flask(__name__)

@app.route('/')
def main():
    # 获取提前存好的构建 select 下拉框的数据
    freqs = np.loadtxt("../clean_data/freq.txt")
    phis = np.loadtxt("../clean_data/phi.txt")
    return render_template('index.html',
                    freqs = freqs,
                    phis = phis)
                    
@app.route('/draw', methods=['POST'])
def draw_render():
    if request.method == 'POST' and request.form.get('freq', 'phi'):
        datax = request.form.to_dict()
        freq = float(datax['freq'])
        phi = float(datax['phi'])
    phi = phi * np.pi / 180
    print(freq, phi)
    line = draw(freq, phi)
    return render_template(
           'pyecharts.html',
           myechart=line.render_embed(),
           host=REMOTE_HOST,
           script_list=line.get_js_dependencies())

def draw(freq_input, phi_input):
    # 获取之前处理的作为x轴取值的theta函数
    attr = np.round(np.loadtxt("../clean_data/theta.txt"),3)
    result = mapreduce(freq_input, phi_input)
    res1 = [doc['value']['values'] for doc in result.find()][0]
    print(res1)
    line = Line("theta角度vs电场作图")
    line.add("Electrial Field1", attr, res1, is_smooth=True,
            xaxis_name = 'Theta(degree)', yaxis_name = 'Electrical field (V/m)',
            xaxis_name_gap = 30, yaxis_name_gap = 40,
            mark_point = ['max', 'min'], mark_point_textcolor = 'black')
            
    return line

# 构建 mapreduce 查询
def mapreduce(freq_input, phi_input):
    # map 函数
    mapfun = Code("""
                    function(){
                        emit({freqs:this.freq, phis:this.phi}, {values: this.vals});
                    }
                """)

        
    # reduce 函数
    reducefun = Code("""
                    function(key, value) {
                        var res = { values: value };
                        return res;
                    }
                """)
    result = my_set.map_reduce(mapfun, reducefun, query={"freq":freq_input, "phi":phi_input},out="test")
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)