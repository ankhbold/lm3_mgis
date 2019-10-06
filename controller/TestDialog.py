__author__ = 'B.Ankhbold'
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QDialog

from ..view.Ui_TestDialog import *
import pickle
import pandas as pd
import numpy as np

class TestDialog(QDialog, Ui_TestDialog):

    def __init__(self, parent=None):

        super(TestDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(self.tr("About Landmanager III"))

    @pyqtSlot()
    def on_test_button_clicked(self):

        print ("test")
        x = 109.189130358
        y = 47.179635092
        with open('D:/work/2018_projects/3_PAYMENT/CAMA/PKL/fwland_valuationfiles/model.pkl', 'rb') as f:
            model_pkl = pickle.load(f)
            print (model_pkl)
            print ('*********')

        with open('D:/work/2018_projects/3_PAYMENT/CAMA/PKL/fwland_valuationfiles/cluster.pkl', 'rb') as f:
            cluster_pkl = pickle.load(f)
            print (cluster_pkl)
            print ('*********')

        with open('D:/work/2018_projects/3_PAYMENT/CAMA/PKL/fwland_valuationfiles/encoder.pkl', 'rb') as f:
            encoder_pkl = pickle.load(f)
            print (encoder_pkl)
            print ('**********')

        # cluster_pkl = pickle.load(open('D:\work\\2018_projects\\3_PAYMENT\CAMA\PKL\\fwland_valuationfiles\cluster.pkl', 'rb'))
        # encoder_pkl = pickle.load(open('D:\work\\2018_projects\\3_PAYMENT\CAMA\PKL\\fwland_valuationfiles\encoder.pkl', 'rb'))

        # # ----------------------------
        # # Test model
        # # ----------------------------
        # print('Enter the land information: \n')
        #
        # Gazriin medeellvvdiig neg bvrchlen zaaval oruulna. Dutuu oruulj bolohgui
        _area = float(400)  # 400
        _X = float(x)  # 106.1
        _Y = float(y)  # 47.9
        _dist_school = int(2100) / 1000  # 2100
        _dist_kinter = int(1600) / 1000  # 2100
        _dist_hosp = int(1500) / 1000  # 2100
        _dist_center = int(2600) / 1000  # 2100
        _level = int(1250) / 1000  # 1250
        _angle = int(15)  # 15
        _risk_flood = int(2)  # 2
        _soil_cont = int(3)  # 3

        # cluster.pkl ashiglan deer oruulsan lat (_Y), long (_X) -g clustert huvaarilna
        print (cluster_pkl)
        print (type(cluster_pkl))
        print (cluster_pkl.predict(pd.DataFrame({'X': [_X], 'Y': [_Y]})))
        _cluster = np.asscalar(cluster_pkl.predict(pd.DataFrame({'X': [_X], 'Y': [_Y]})))
        # _cluster = 18
        print (_cluster)
        # Put input into a dataframe
        # Medeelluudee neg dataframe-d oruuliy
        _df = pd.DataFrame({'dist_school': _dist_school,
                            'dist_kinter': _dist_kinter,
                            'dist_hosp': _dist_hosp,
                            'level': _level,
                            'angle': _angle,
                            'dist_center': _dist_center,
                            'risk_flood': _risk_flood,
                            'soil_cont': _soil_cont,
                            'cluster': _cluster},
                           index=np.arange(1))
        print (_df)
        print (np.array(_df.cluster).reshape(-1, 1))
        # # One hot encoding ashiglan clusteriin dugaariig olon baganatai  dummy huvisagchid huvirgana
        _array_onehot = encoder_pkl.transform(np.array(_df.cluster).reshape(-1, 1))
        #
        # # Garaas oruulsan ogogdliig zagvariin input formataar beltgene
        _X = np.column_stack((_array_onehot,
                              _df.iloc[:, 0:-1].values))
        #
        # # Prediction results
        # # model.pkl ashiglan taamaglaliin vr dvng gargana. Zagvar unelehdee "log(x+1)/1000" huvirgalt anhnasaa hiisen baisan tul inverse transformation hiih buyu "(exp(x)-1)*1000"
        _pred_pkl = (np.exp(np.asscalar(model_pkl.predict(_X))) - 1) * 1000
        #
        # # Deer garsan taamaglal ni 1m2-n vniig haruulah tul _area-r vrjij niit vniig olno
        result = '{:,.0f} ₮'.format(_pred_pkl * _area)
        print('Land price is estimated as {}'.format(result))

    @pyqtSlot()
    def on_close_button_clicked(self):

        self.reject()