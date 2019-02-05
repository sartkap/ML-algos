{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.57696045]\n",
      " [0.88481726]]\n",
      "[[  0   0   0   0   0   0   0   0   0   0]\n",
      " [  0   1   5   6  10   9  13  16   5  18]\n",
      " [  0   5  25  30  50  45  65  80  25  90]\n",
      " [  0   6  30  36  60  54  78  96  30 108]\n",
      " [  0  10  50  60 100  90 130 160  50 180]\n",
      " [  0   9  45  54  90  81 117 144  45 162]\n",
      " [  0  13  65  78 130 117 169 208  65 234]\n",
      " [  0  16  80  96 160 144 208 256  80 288]\n",
      " [  0   5  25  30  50  45  65  80  25  90]\n",
      " [  0  18  90 108 180 162 234 288  90 324]]\n",
      "115.5399178101799\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x7f0df92d7208>]"
      ]
     },
     "execution_count": 103,
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
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "x = np.array([1,2,3,4,5,6,7,8,9,10])\n",
    "#print(x)\n",
    "y =np.array([0,1,5,6,10,9,13,16,5,18])[np.newaxis]\n",
    "#print(y)\n",
    "w=np.random.rand(2,1)\n",
    "print(w)\n",
    "#X=np.linspace(0,10,10)\n",
    "#print(X)\n",
    "y_p=w[0]*x + w[1]\n",
    "#print(y_p)\n",
    "#plt.scatter(x,y)\n",
    "#plt.show()\n",
    "#eps = 1\n",
    "print(np.transpose(y)*y)\n",
    "#print((y-y_p)*np.transpose(y-y_p))\n",
    "alpha = 0.0009\n",
    "\n",
    "for i in range(400):\n",
    "    grad_m=-2*((y-y_p)*x).sum()\n",
    "    grad_c=-2*((y-y_p)).sum()\n",
    "    y_p=w[0]*x + w[1]\n",
    "    w[0]=w[0]-alpha*grad_m\n",
    "    w[1]=w[1]-alpha*grad_c\n",
    "    loss=((y-y_p)*(y-y_p)).sum()\n",
    "print(loss)\n",
    "plt.scatter(x,y)\n",
    "plt.plot(x,y_p)    \n"
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
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
