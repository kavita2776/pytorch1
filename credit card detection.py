{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ec4389d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ef75d722",
   "metadata": {},
   "outputs": [],
   "source": [
    "df= pd.read_csv('creditcard.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "767e5c13",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Time</th>\n",
       "      <th>V1</th>\n",
       "      <th>V2</th>\n",
       "      <th>V3</th>\n",
       "      <th>V4</th>\n",
       "      <th>V5</th>\n",
       "      <th>V6</th>\n",
       "      <th>V7</th>\n",
       "      <th>V8</th>\n",
       "      <th>V9</th>\n",
       "      <th>...</th>\n",
       "      <th>V21</th>\n",
       "      <th>V22</th>\n",
       "      <th>V23</th>\n",
       "      <th>V24</th>\n",
       "      <th>V25</th>\n",
       "      <th>V26</th>\n",
       "      <th>V27</th>\n",
       "      <th>V28</th>\n",
       "      <th>Amount</th>\n",
       "      <th>Class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.0</td>\n",
       "      <td>-1.359807</td>\n",
       "      <td>-0.072781</td>\n",
       "      <td>2.536347</td>\n",
       "      <td>1.378155</td>\n",
       "      <td>-0.338321</td>\n",
       "      <td>0.462388</td>\n",
       "      <td>0.239599</td>\n",
       "      <td>0.098698</td>\n",
       "      <td>0.363787</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.018307</td>\n",
       "      <td>0.277838</td>\n",
       "      <td>-0.110474</td>\n",
       "      <td>0.066928</td>\n",
       "      <td>0.128539</td>\n",
       "      <td>-0.189115</td>\n",
       "      <td>0.133558</td>\n",
       "      <td>-0.021053</td>\n",
       "      <td>149.62</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.0</td>\n",
       "      <td>1.191857</td>\n",
       "      <td>0.266151</td>\n",
       "      <td>0.166480</td>\n",
       "      <td>0.448154</td>\n",
       "      <td>0.060018</td>\n",
       "      <td>-0.082361</td>\n",
       "      <td>-0.078803</td>\n",
       "      <td>0.085102</td>\n",
       "      <td>-0.255425</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.225775</td>\n",
       "      <td>-0.638672</td>\n",
       "      <td>0.101288</td>\n",
       "      <td>-0.339846</td>\n",
       "      <td>0.167170</td>\n",
       "      <td>0.125895</td>\n",
       "      <td>-0.008983</td>\n",
       "      <td>0.014724</td>\n",
       "      <td>2.69</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.0</td>\n",
       "      <td>-1.358354</td>\n",
       "      <td>-1.340163</td>\n",
       "      <td>1.773209</td>\n",
       "      <td>0.379780</td>\n",
       "      <td>-0.503198</td>\n",
       "      <td>1.800499</td>\n",
       "      <td>0.791461</td>\n",
       "      <td>0.247676</td>\n",
       "      <td>-1.514654</td>\n",
       "      <td>...</td>\n",
       "      <td>0.247998</td>\n",
       "      <td>0.771679</td>\n",
       "      <td>0.909412</td>\n",
       "      <td>-0.689281</td>\n",
       "      <td>-0.327642</td>\n",
       "      <td>-0.139097</td>\n",
       "      <td>-0.055353</td>\n",
       "      <td>-0.059752</td>\n",
       "      <td>378.66</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1.0</td>\n",
       "      <td>-0.966272</td>\n",
       "      <td>-0.185226</td>\n",
       "      <td>1.792993</td>\n",
       "      <td>-0.863291</td>\n",
       "      <td>-0.010309</td>\n",
       "      <td>1.247203</td>\n",
       "      <td>0.237609</td>\n",
       "      <td>0.377436</td>\n",
       "      <td>-1.387024</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.108300</td>\n",
       "      <td>0.005274</td>\n",
       "      <td>-0.190321</td>\n",
       "      <td>-1.175575</td>\n",
       "      <td>0.647376</td>\n",
       "      <td>-0.221929</td>\n",
       "      <td>0.062723</td>\n",
       "      <td>0.061458</td>\n",
       "      <td>123.50</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2.0</td>\n",
       "      <td>-1.158233</td>\n",
       "      <td>0.877737</td>\n",
       "      <td>1.548718</td>\n",
       "      <td>0.403034</td>\n",
       "      <td>-0.407193</td>\n",
       "      <td>0.095921</td>\n",
       "      <td>0.592941</td>\n",
       "      <td>-0.270533</td>\n",
       "      <td>0.817739</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.009431</td>\n",
       "      <td>0.798278</td>\n",
       "      <td>-0.137458</td>\n",
       "      <td>0.141267</td>\n",
       "      <td>-0.206010</td>\n",
       "      <td>0.502292</td>\n",
       "      <td>0.219422</td>\n",
       "      <td>0.215153</td>\n",
       "      <td>69.99</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 31 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   Time        V1        V2        V3        V4        V5        V6        V7  \\\n",
       "0   0.0 -1.359807 -0.072781  2.536347  1.378155 -0.338321  0.462388  0.239599   \n",
       "1   0.0  1.191857  0.266151  0.166480  0.448154  0.060018 -0.082361 -0.078803   \n",
       "2   1.0 -1.358354 -1.340163  1.773209  0.379780 -0.503198  1.800499  0.791461   \n",
       "3   1.0 -0.966272 -0.185226  1.792993 -0.863291 -0.010309  1.247203  0.237609   \n",
       "4   2.0 -1.158233  0.877737  1.548718  0.403034 -0.407193  0.095921  0.592941   \n",
       "\n",
       "         V8        V9  ...       V21       V22       V23       V24       V25  \\\n",
       "0  0.098698  0.363787  ... -0.018307  0.277838 -0.110474  0.066928  0.128539   \n",
       "1  0.085102 -0.255425  ... -0.225775 -0.638672  0.101288 -0.339846  0.167170   \n",
       "2  0.247676 -1.514654  ...  0.247998  0.771679  0.909412 -0.689281 -0.327642   \n",
       "3  0.377436 -1.387024  ... -0.108300  0.005274 -0.190321 -1.175575  0.647376   \n",
       "4 -0.270533  0.817739  ... -0.009431  0.798278 -0.137458  0.141267 -0.206010   \n",
       "\n",
       "        V26       V27       V28  Amount  Class  \n",
       "0 -0.189115  0.133558 -0.021053  149.62      0  \n",
       "1  0.125895 -0.008983  0.014724    2.69      0  \n",
       "2 -0.139097 -0.055353 -0.059752  378.66      0  \n",
       "3 -0.221929  0.062723  0.061458  123.50      0  \n",
       "4  0.502292  0.219422  0.215153   69.99      0  \n",
       "\n",
       "[5 rows x 31 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "54773c29",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Time      0\n",
       "V1        0\n",
       "V2        0\n",
       "V3        0\n",
       "V4        0\n",
       "V5        0\n",
       "V6        0\n",
       "V7        0\n",
       "V8        0\n",
       "V9        0\n",
       "V10       0\n",
       "V11       0\n",
       "V12       0\n",
       "V13       0\n",
       "V14       0\n",
       "V15       0\n",
       "V16       0\n",
       "V17       0\n",
       "V18       0\n",
       "V19       0\n",
       "V20       0\n",
       "V21       0\n",
       "V22       0\n",
       "V23       0\n",
       "V24       0\n",
       "V25       0\n",
       "V26       0\n",
       "V27       0\n",
       "V28       0\n",
       "Amount    0\n",
       "Class     0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5f49f15a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Time</th>\n",
       "      <th>V1</th>\n",
       "      <th>V2</th>\n",
       "      <th>V3</th>\n",
       "      <th>V4</th>\n",
       "      <th>V5</th>\n",
       "      <th>V6</th>\n",
       "      <th>V7</th>\n",
       "      <th>V8</th>\n",
       "      <th>V9</th>\n",
       "      <th>...</th>\n",
       "      <th>V20</th>\n",
       "      <th>V21</th>\n",
       "      <th>V22</th>\n",
       "      <th>V23</th>\n",
       "      <th>V24</th>\n",
       "      <th>V25</th>\n",
       "      <th>V26</th>\n",
       "      <th>V27</th>\n",
       "      <th>V28</th>\n",
       "      <th>Amount</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Class</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "      <td>...</td>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "      <td>284315</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "      <td>...</td>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "      <td>492</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2 rows × 30 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         Time      V1      V2      V3      V4      V5      V6      V7      V8  \\\n",
       "Class                                                                           \n",
       "0      284315  284315  284315  284315  284315  284315  284315  284315  284315   \n",
       "1         492     492     492     492     492     492     492     492     492   \n",
       "\n",
       "           V9  ...     V20     V21     V22     V23     V24     V25     V26  \\\n",
       "Class          ...                                                           \n",
       "0      284315  ...  284315  284315  284315  284315  284315  284315  284315   \n",
       "1         492  ...     492     492     492     492     492     492     492   \n",
       "\n",
       "          V27     V28  Amount  \n",
       "Class                          \n",
       "0      284315  284315  284315  \n",
       "1         492     492     492  \n",
       "\n",
       "[2 rows x 30 columns]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby(['Class']).count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "bdbdae09",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = df.drop(['Time','Class'],axis=1)\n",
    "y = df.iloc[:,-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a0d64a7a",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "40e088a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e5e7ca12",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "948a1887",
   "metadata": {},
   "outputs": [],
   "source": [
    "model =  LogisticRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "57f232c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\kp272\\anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_logistic.py:444: ConvergenceWarning: lbfgs failed to converge (status=1):\n",
      "STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.\n",
      "\n",
      "Increase the number of iterations (max_iter) or scale the data as shown in:\n",
      "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
      "Please also refer to the documentation for alternative solver options:\n",
      "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
      "  n_iter_i = _check_optimize_result(\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LogisticRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LogisticRegression</label><div class=\"sk-toggleable__content\"><pre>LogisticRegression()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "LogisticRegression()"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "64da73e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.999180730788137"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.score(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "5dda1cc7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9992275497879273"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.score(x_test,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "be445751",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import classification_report"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "538687e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred = model.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "9d68cadd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       1.00      1.00      1.00     71082\n",
      "           1       0.87      0.63      0.73       120\n",
      "\n",
      "    accuracy                           1.00     71202\n",
      "   macro avg       0.94      0.82      0.87     71202\n",
      "weighted avg       1.00      1.00      1.00     71202\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(classification_report(y_test,y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "2726ed98",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: imblearn in c:\\users\\kp272\\anaconda3\\lib\\site-packages (0.0)\n",
      "Requirement already satisfied: imbalanced-learn in c:\\users\\kp272\\anaconda3\\lib\\site-packages (from imblearn) (0.9.1)\n",
      "Requirement already satisfied: numpy>=1.17.3 in c:\\users\\kp272\\anaconda3\\lib\\site-packages (from imbalanced-learn->imblearn) (1.20.3)\n",
      "Requirement already satisfied: threadpoolctl>=2.0.0 in c:\\users\\kp272\\anaconda3\\lib\\site-packages (from imbalanced-learn->imblearn) (2.2.0)\n",
      "Requirement already satisfied: scikit-learn>=1.1.0 in c:\\users\\kp272\\anaconda3\\lib\\site-packages (from imbalanced-learn->imblearn) (1.1.1)\n",
      "Requirement already satisfied: scipy>=1.3.2 in c:\\users\\kp272\\anaconda3\\lib\\site-packages (from imbalanced-learn->imblearn) (1.7.1)\n",
      "Requirement already satisfied: joblib>=1.0.0 in c:\\users\\kp272\\anaconda3\\lib\\site-packages (from imbalanced-learn->imblearn) (1.1.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install imblearn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "2ad52a13",
   "metadata": {},
   "outputs": [],
   "source": [
    "from imblearn.over_sampling import SMOTE "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "c67b4bf9",
   "metadata": {},
   "outputs": [],
   "source": [
    "upsample = SMOTE()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "66ec6aaf",
   "metadata": {},
   "outputs": [],
   "source": [
    "x,y = upsample.fit_resample(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "875c60f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import Counter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "1e516c27",
   "metadata": {},
   "outputs": [],
   "source": [
    "count = Counter(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "45ea051a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Counter({0: 284315, 1: 284315})\n"
     ]
    }
   ],
   "source": [
    "print(count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "f5600efb",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "0e0b14e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\kp272\\anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_logistic.py:444: ConvergenceWarning: lbfgs failed to converge (status=1):\n",
      "STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.\n",
      "\n",
      "Increase the number of iterations (max_iter) or scale the data as shown in:\n",
      "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
      "Please also refer to the documentation for alternative solver options:\n",
      "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
      "  n_iter_i = _check_optimize_result(\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LogisticRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" checked><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LogisticRegression</label><div class=\"sk-toggleable__content\"><pre>LogisticRegression()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "LogisticRegression()"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "5d933ded",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9582973794293647"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.score(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "d4a893f9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9581099902924914"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.score(x_test,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "a89980a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred = model.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "72c5cc57",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.94      0.98      0.96     70856\n",
      "           1       0.98      0.94      0.96     71302\n",
      "\n",
      "    accuracy                           0.96    142158\n",
      "   macro avg       0.96      0.96      0.96    142158\n",
      "weighted avg       0.96      0.96      0.96    142158\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(classification_report(y_test,y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "42f69a77",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2733aab4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
