{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "K6uszEF-tg6Q"
   },
   "source": [
    "# Unsupervised Machine Learning - KMeans\n",
    "\n",
    "Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection. SVMs are one of the most robust prediction methods. \n",
    "\n",
    "Sources: \n",
    "[sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html?highlight=kmeans#sklearn.cluster.KMeans), [wikipedia](https://en.wikipedia.org/wiki/K-means_clustering)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "fUB89AR6C5Br"
   },
   "source": [
    "![kmeans.png](https://www.mathworks.com/matlabcentral/mlc-downloads/downloads/submissions/52579/versions/9/screenshot.jpg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn import datasets\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Take make moons in built dataset\n",
    "\n",
    "data_ = "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([[-3.45365054e-01,  9.38468422e-01],\n",
       "        [ 9.26916757e-01,  3.75267005e-01],\n",
       "        [ 3.27051370e-02,  2.46345416e-01],\n",
       "        [ 7.15472413e-01, -4.58667853e-01],\n",
       "        [-3.20515776e-02,  9.99486216e-01],\n",
       "        [ 9.97945393e-01,  6.40702200e-02],\n",
       "        [ 1.94905575e+00,  1.84891782e-01],\n",
       "        [ 1.61911895e-01, -4.55349012e-02],\n",
       "        [ 9.67294863e-01,  2.53654584e-01],\n",
       "        [ 5.72116660e-01,  8.20172255e-01],\n",
       "        [ 7.61445958e-01,  6.48228395e-01],\n",
       "        [ 8.40400105e-01, -4.87181783e-01],\n",
       "        [ 2.00000000e+00,  5.00000000e-01],\n",
       "        [ 8.38088105e-01,  5.45534901e-01],\n",
       "        [ 1.57211666e+00, -3.20172255e-01],\n",
       "        [-7.61445958e-01,  6.48228395e-01],\n",
       "        [-9.97945393e-01,  6.40702200e-02],\n",
       "        [-9.91790014e-01,  1.27877162e-01],\n",
       "        [-4.62538290e-01,  8.86599306e-01],\n",
       "        [-2.22520934e-01,  9.74927912e-01],\n",
       "        [ 1.34536505e+00, -4.38468422e-01],\n",
       "        [ 5.95216657e-01, -4.14412623e-01],\n",
       "        [ 9.00968868e-01,  4.33883739e-01],\n",
       "        [ 8.01413622e-01,  5.98110530e-01],\n",
       "        [ 2.84527587e-01,  9.58667853e-01],\n",
       "        [-6.72300890e-01,  7.40277997e-01],\n",
       "        [ 7.30832427e-02,  1.24732995e-01],\n",
       "        [ 1.15959990e+00, -4.87181783e-01],\n",
       "        [ 8.71318704e-01,  4.90717552e-01],\n",
       "        [ 7.18349350e-01,  6.95682551e-01],\n",
       "        [ 1.98586378e-01, -9.81105305e-02],\n",
       "        [ 1.71834935e+00, -1.95682551e-01],\n",
       "        [ 3.20515776e-02,  9.99486216e-01],\n",
       "        [ 9.67948422e-01, -4.99486216e-01],\n",
       "        [ 1.87131870e+00,  9.28244800e-03],\n",
       "        [ 1.76144596e+00, -1.48228395e-01],\n",
       "        [-1.59599895e-01,  9.87181783e-01],\n",
       "        [-5.72116660e-01,  8.20172255e-01],\n",
       "        [ 3.45365054e-01,  9.38468422e-01],\n",
       "        [ 1.99179001e+00,  3.72122838e-01],\n",
       "        [ 6.23489802e-01,  7.81831482e-01],\n",
       "        [ 4.04783343e-01,  9.14412623e-01],\n",
       "        [ 5.09442530e-02,  1.84891782e-01],\n",
       "        [ 6.72300890e-01,  7.40277997e-01],\n",
       "        [ 9.90311321e-02,  6.61162609e-02],\n",
       "        [-9.00968868e-01,  4.33883739e-01],\n",
       "        [-8.71318704e-01,  4.90717552e-01],\n",
       "        [ 7.77479066e-01, -4.74927912e-01],\n",
       "        [-8.38088105e-01,  5.45534901e-01],\n",
       "        [-9.81559157e-01,  1.91158629e-01],\n",
       "        [ 4.81607432e-01, -3.55142763e-01],\n",
       "        [ 1.28452759e+00, -4.58667853e-01],\n",
       "        [-8.01413622e-01,  5.98110530e-01],\n",
       "        [-2.84527587e-01,  9.58667853e-01],\n",
       "        [ 2.81650650e-01, -1.95682551e-01],\n",
       "        [ 1.46253829e+00, -3.86599306e-01],\n",
       "        [ 9.81559157e-01,  1.91158629e-01],\n",
       "        [ 1.84408430e-02,  3.08841371e-01],\n",
       "        [ 1.59599895e-01,  9.87181783e-01],\n",
       "        [ 2.05460725e-03,  4.35929780e-01],\n",
       "        [ 1.92691676e+00,  1.24732995e-01],\n",
       "        [-1.00000000e+00,  1.22464680e-16],\n",
       "        [ 1.51839257e+00, -3.55142763e-01],\n",
       "        [ 1.98155916e+00,  3.08841371e-01],\n",
       "        [ 9.03976974e-01, -4.95379113e-01],\n",
       "        [ 4.62538290e-01,  8.86599306e-01],\n",
       "        [ 9.91790014e-01,  1.27877162e-01],\n",
       "        [ 8.20998618e-03,  3.72122838e-01],\n",
       "        [-9.49055747e-01,  3.15108218e-01],\n",
       "        [-9.67294863e-01,  2.53654584e-01],\n",
       "        [ 1.28681296e-01,  9.28244800e-03],\n",
       "        [ 1.96729486e+00,  2.46345416e-01],\n",
       "        [ 6.54634946e-01, -4.38468422e-01],\n",
       "        [ 1.40478334e+00, -4.14412623e-01],\n",
       "        [ 1.09602303e+00, -4.95379113e-01],\n",
       "        [-6.23489802e-01,  7.81831482e-01],\n",
       "        [ 5.37461710e-01, -3.86599306e-01],\n",
       "        [-4.04783343e-01,  9.14412623e-01],\n",
       "        [ 4.27883340e-01, -3.20172255e-01],\n",
       "        [-5.18392568e-01,  8.55142763e-01],\n",
       "        [ 1.00000000e+00,  0.00000000e+00],\n",
       "        [ 9.49055747e-01,  3.15108218e-01],\n",
       "        [-7.18349350e-01,  6.95682551e-01],\n",
       "        [ 1.03205158e+00, -4.99486216e-01],\n",
       "        [ 1.83808810e+00, -4.55349012e-02],\n",
       "        [-9.26916757e-01,  3.75267005e-01],\n",
       "        [ 1.67230089e+00, -2.40277997e-01],\n",
       "        [ 1.22252093e+00, -4.74927912e-01],\n",
       "        [ 1.80141362e+00, -9.81105305e-02],\n",
       "        [ 9.60230259e-02,  9.95379113e-01],\n",
       "        [ 2.22520934e-01,  9.74927912e-01],\n",
       "        [ 1.90096887e+00,  6.61162609e-02],\n",
       "        [ 3.27699110e-01, -2.40277997e-01],\n",
       "        [-9.60230259e-02,  9.95379113e-01],\n",
       "        [ 2.38554042e-01, -1.48228395e-01],\n",
       "        [ 0.00000000e+00,  5.00000000e-01],\n",
       "        [ 1.62348980e+00, -2.81831482e-01],\n",
       "        [ 3.76510198e-01, -2.81831482e-01],\n",
       "        [ 5.18392568e-01,  8.55142763e-01],\n",
       "        [ 1.99794539e+00,  4.35929780e-01]]),\n",
       " array([0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1,\n",
       "        0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0,\n",
       "        1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0,\n",
       "        0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1,\n",
       "        1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1], dtype=int64))"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# check the dataset\n",
    "\n",
    "data_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# create input dataframe\n",
    "\n",
    "inputData = "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
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
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>-0.345365</td>\n",
       "      <td>0.938468</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.926917</td>\n",
       "      <td>0.375267</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.032705</td>\n",
       "      <td>0.246345</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.715472</td>\n",
       "      <td>-0.458668</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>-0.032052</td>\n",
       "      <td>0.999486</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          0         1\n",
       "0 -0.345365  0.938468\n",
       "1  0.926917  0.375267\n",
       "2  0.032705  0.246345\n",
       "3  0.715472 -0.458668\n",
       "4 -0.032052  0.999486"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inputData.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
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
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   0\n",
       "0  0\n",
       "1  0\n",
       "2  1\n",
       "3  1\n",
       "4  0"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# create output dataframe\n",
    "\n",
    "outputData = \n",
    "outputData.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x1a38e535ac0>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# create a scatter plot for inputData set\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x1a38e5948b0>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# create a scatter plot for inputData set with outputData color\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KMeans(n_clusters=5)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Call the sklearn Kmeans and make a model with 200 samples\n",
    "\n",
    "\n",
    "#model_fit\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 0, 1, 3, 1, 0, 2, 3, 0, 0, 0, 3, 2, 0, 2, 4, 4, 4, 1, 1, 2, 3,\n",
       "       0, 0, 1, 4, 3, 2, 0, 0, 3, 2, 1, 3, 2, 2, 1, 4, 1, 2, 0, 1, 1, 0,\n",
       "       3, 4, 4, 3, 4, 4, 3, 2, 4, 1, 3, 2, 0, 1, 1, 1, 2, 4, 2, 2, 3, 1,\n",
       "       0, 1, 4, 4, 3, 2, 3, 2, 3, 4, 3, 1, 3, 4, 0, 0, 4, 3, 2, 4, 2, 2,\n",
       "       2, 1, 1, 2, 3, 1, 3, 1, 2, 3, 1, 2])"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# check for labels\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.4734072067815621"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# call metrics and check silhoutte score\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x1a38ff9f7c0>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# create a scatter plot for inputData set with model labels color\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### finding right number of cluster"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "cluster_range = range(1, 20)\n",
    "error_list = []\n",
    "\n",
    "for i in cluster_range:\n",
    "    model = KMeans(n_clusters=i)\n",
    "    model.fit(inputData)\n",
    "    res = model.inertia_\n",
    "    error_list.append(res)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "plt.plot(cluster_range, error_list, marker = \"o\", color = \"g\", markersize = 10)\n",
    "plt.xlabel(\"Cluster Range\")\n",
    "plt.ylabel(\"IntraCluster Sum\")\n",
    "plt.title(\"KMeans\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

