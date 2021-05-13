from flask import Flask, render_template, request, send_from_directory
from ast import literal_eval
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import re,time
from Classes.PrimAlgorithm import PrimAlgo
from Classes.KrushKalAlgorithm import KrushkalAlgo
app = Flask(__name__,static_url_path='',
            static_folder='Images',
            template_folder='Templates')

@app.route('/minspantree',methods = ['POST'])
def minspantree():
    mstOutput=[]
    mstalgo=request.form.getlist('mstalgo')
    pattern = re.compile(r'\s+')
    inputvertices=re.sub(pattern, '', request.form['inputVertex'])
    inputedges=re.sub(pattern, '', request.form['inputEdges'])
    numbercheck=all(item.isnumeric() for item in inputvertices.split(','))
    if(len(mstalgo)==0):
        return "Please select the Algorithm"
    else:
        if(numbercheck):
            verticies=[int(item) for item in inputvertices.split(',')]
            verticies.sort()
            edges = [tuple(item) for item in literal_eval(inputedges)]
        else:
            verticies = inputvertices.split(',')
            verticies.sort()
            edges = [(item.split(',')[0],item.split(',')[1],int(item.split(',')[-1])) for item in inputedges.replace('),(','*').replace('(','').replace(')','').split('*')]
        for algo in mstalgo:
            if(algo.lower()=="prim"):
                prims= PrimAlgo(verticies, edges)
                start_time = time.perf_counter()
                result=prims.getMinSpanTree()
                totalcost= sum([pair[2] for pair in result])
                primsExecutionTime=time.perf_counter() - start_time
                output={
                    "Algorithm":"Prims",
                    "Input Verticies":verticies,
                    "Input Edges":edges,
                    "Number of Input Verticies":len(verticies),
                    "Number of Input Edges":len(edges),
                    "Minimum SpanningTree":result,
                    "Total Cost":totalcost,
                    "Execution Time in Seconds":str(primsExecutionTime)
                    }
                G = nx.Graph()
                element=0
                for node in verticies:
                    if(element%2==0):
                        G.add_node(node,pos=(element,element+2))
                    else:
                        G.add_node(node, pos=(element+1, element-1))
                    element += 1
                for edge in result:
                    G.add_edge(edge[0],edge[1], weight=edge[2])
                pos = nx.get_node_attributes(G,'pos')
                nx.draw(G, pos,with_labels = True)
                labels = nx.get_edge_attributes(G, 'weight')
                nx.draw_networkx_edge_labels(G, pos, edge_labels=labels,font_size=5)
                primsFileName = 'primsoutput'+str(time.time())+'.jpg'
                mstOutput.append((primsFileName,output))
                plt.savefig('./Images/'+primsFileName)
                plt.cla()
                plt.clf()
                del G
                del prims
            else:
                krushkal = KrushkalAlgo(verticies, edges)
                start_time = time.perf_counter()
                result = krushkal.getMinSpanTree()
                totalcost = sum([pair[2] for pair in result])
                krushkalExecutionTime = time.perf_counter() - start_time
                output={
                "Algorithm":"Krushkal",
                "Input Verticies": verticies,
                "Input Edges": edges,
                "Number of Input Verticies": len(verticies),
                "Number of Input Edges": len(edges),
                "Minimum SpanningTree": result,
                "Total Cost": totalcost,
                "Execution Time in Seconds": str(krushkalExecutionTime)
                }
                G = nx.Graph()
                element=0
                for node in verticies:
                    if (element % 2 == 0):
                        G.add_node(node, pos=(element+1, element))
                    else:
                        G.add_node(node, pos=(element-1, element+2))
                    element += 1
                for edge in result:
                    G.add_edge(edge[0],edge[1], weight=edge[2])
                pos = nx.get_node_attributes(G,'pos')
                nx.draw(G, pos,with_labels = True)
                labels = nx.get_edge_attributes(G, 'weight')
                nx.draw_networkx_edge_labels(G, pos, edge_labels=labels,font_size=5)
                krushkalFileName = 'krushkaloutput'+str(time.time())+'.jpg'
                mstOutput.append((krushkalFileName,output))
                krushkalResult='./Images/'+krushkalFileName
                plt.savefig(krushkalResult)
                plt.cla()
                plt.clf()
                del G
                del krushkal
        algo=[item[1]['Algorithm'] for item in mstOutput]
        executionTime = [float(item[1]['Execution Time in Seconds']) for item in mstOutput]
        plt.bar(algo, executionTime, width=0.6)
        plt.title('Algorithm VS Execution Time')
        plt.xlabel('Algorithms')
        plt.ylabel('Execution Time in Seconds')
        perfGraphname = 'algobarchart' + str(time.time()) + '.jpg'
        bargraphPath= './Images/' + perfGraphname
        plt.savefig(bargraphPath)
        plt.cla()
        plt.clf()
        return render_template("output.html",mstoutput=mstOutput,perfGraphname=perfGraphname)
@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("images", path)
@app.route("/")
def MainPage():
    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)

