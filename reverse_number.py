{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e3eafe09-ccf3-4c09-b056-3010d5daecb8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "  1234\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4321\n"
     ]
    }
   ],
   "source": [
    "n=int(input(' '))\n",
    "r=0\n",
    "while(n>0):\n",
    "    digit=n%10\n",
    "    r=r*10+digit\n",
    "    n=n//10\n",
    "print(r)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb9d9bcf-0d7f-4b36-aa5c-cade69be8ab6",
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
