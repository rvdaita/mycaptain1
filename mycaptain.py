{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter number of terms :10\n",
      "0 1 1 2 3 5 8 13 21 34 "
     ]
    }
   ],
   "source": [
    "n = int(input(\"enter number of terms :\"))\n",
    "first = 0\n",
    "second = 1\n",
    "print(first,second,end=\" \")\n",
    "for i in range(n - 2):\n",
    "    third = first + second\n",
    "    print(third,end=\" \")\n",
    "    first = second\n",
    "    second = third    "
   ]
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
