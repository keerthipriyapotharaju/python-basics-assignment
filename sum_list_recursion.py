{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a6e2e464-310e-45a7-aac5-3690335314de",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "sum() takes 1 positional argument but 4 were given",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[7], line 6\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m      5\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m n[\u001b[38;5;241m0\u001b[39m]\u001b[38;5;241m+\u001b[39m\u001b[38;5;28msum\u001b[39m(n[\u001b[38;5;241m1\u001b[39m:])\n\u001b[1;32m----> 6\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;28msum\u001b[39m(\u001b[38;5;241m1\u001b[39m,\u001b[38;5;241m2\u001b[39m,\u001b[38;5;241m3\u001b[39m,\u001b[38;5;241m4\u001b[39m))\n",
      "\u001b[1;31mTypeError\u001b[0m: sum() takes 1 positional argument but 4 were given"
     ]
    }
   ],
   "source": [
    "def sum(n):\n",
    "    if not n:\n",
    "        return 0\n",
    "    else:\n",
    "        return n[0]+sum(n[1:])\n",
    "print(sum(1,2,3,4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73ff30be-2b20-4242-a183-557ab7c69a89",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
