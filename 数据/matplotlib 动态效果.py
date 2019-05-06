import matplotlib.pyplot as plt
import numpy as np
import time
fig = plt.figure()
fig.add_subplot(1,1,1)
po_annotation = []
# 从上到下的y轴线
'''
color	字体颜色：color=‘r’；b、g、r、c、m、y、k、w 或者blue、green、red、cyan、magenta、yellow、black、whtite 或十六进制字符串（’#008000’）
linewidth	线条粗细：linewidth=1.=5.=0.3
linestyle	线条形状：linestyle=’–’(虚线);linestyle=’:’(点线);linestyle=’-.’(短线加点)；
label	数据标签内容：label=‘数据一’,数据标签展示位置需另说明plt.legend(loc=1)数字为标签位置

'''
# plt.axvline(x=1,linestyle=':',color='#cccccc')
for i in range(0, 10):
    x = i
    y = x ** 2
    # 其中k为黑色，o为用圆点标记
    point, = plt.plot(x, y, 'ko')
    # annotation = plt.annotate(('x=' + str(x), 'y=' + str(y)), xy=(x + 0.1, y + 0.1), xycoords='data',
    #                           xytext=(x + 0.7, y + 0.7),
    #                           textcoords='data', horizontalalignment="left",
    #                           arrowprops=dict(arrowstyle="simple", connectionstyle="arc3,rad=-0.1"),
    #                           bbox=dict(boxstyle="round", facecolor="w", edgecolor="0.5", alpha=0.9)
    #                           )
    # annotation = plt.annotate(('x=' + str(x), 'y=' + str(y)), xy=(x - 1, y + 10))
    bbox_props = dict(boxstyle="round,pad=0.3", fc="w", ec="k", lw=1)
    # annotation = plt.text(x,y+15,'x={},y={}'.format(str(x),str(y)),ha='center',va='center',size=15, bbox=bbox_props)
    # annotation.set_visible(False)
    po_annotation.append(point)

bbox_props = dict(boxstyle="round,pad=0.3", fc="w", ec="k", lw=1)
desc = plt.text(1, 1, 'xx', ha='center', va='center', size=15,
         bbox=bbox_props)
line = plt.axvline(x=1, linestyle=':', color='#cccccc')
desc.set_visible(False)
line.set_visible(False)

x1 = np.linspace(0, 10, 66)
y1 = x1 ** 2
plt.plot(x1, y1)

def on_move(event):
    visibility_changed = False
    # x 位置，距离画布左端的像素
    # xdata 鼠标的x坐标，以数据坐标为单位
    mouseX = event.xdata
    mouseY = event.ydata
    for point in po_annotation:
        # 点的坐标
        pointx = point.get_xdata()[0]
        pointy = point.get_ydata()[0]
        if mouseX:
            if pointx - 0.45 < mouseX < pointx + 0.45:
                desc.set_x(mouseX)
                desc.set_y(mouseY)
                desc.set_text('x:{},y:{}'.format(pointx,pointy))

                line.set_xdata(pointx)


                line.set_visible(True)
                desc.set_visible(True)
                visibility_changed = True
        # bbox_props = dict(boxstyle="round,pad=0.3", fc="w", ec="k", lw=1)
        # plt.text(x,y+15,'x={},y={}'.format(str(x),str(y)),ha='center',va='center',size=15, bbox=bbox_props)
        # visibility_changed = True
        # print(point,annotation)
        # should_be_visible = (point.contains(event)[0] == True)
        #
        # if should_be_visible != annotation.get_visible():
        #
        #     annotation.set_visible(should_be_visible)
        #     else:

        if visibility_changed:
            plt.draw()

on_move_id = fig.canvas.mpl_connect('motion_notify_event', on_move)

# 直线：x为10-10,y为0-10
# plt.plot([10,10],[0,10])
# plt.xticks(np.arange(0,10,1))

# plt.axis()
# 获取：结果：值1-x的最小坐标，值2-x的最大坐标，值3-y的最小坐标，值4-y的最大坐标
# print(plt.axis())
# 设置：plt.axis([xmin,xmax,ymin,ymax])
# plt.axis([0,40,0,50])
# plt.xlim() 返回x的最大坐标和最小坐标
# plt.ylim() 返回y的最大坐标和最小坐标
# xmin,xmax,ymin,ymax = plt.axis()




plt.show()