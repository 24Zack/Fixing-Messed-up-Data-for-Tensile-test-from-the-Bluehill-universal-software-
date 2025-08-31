# Fixing-Messed-up-Data-for-Tensile-test-from-the-Bluehill-universal-software-
A solution for when the data is wrong because of the machine's error rather than performing the test a second time
<img width="401" height="476" alt="Screenshot 2025-08-31 at 19 10 10" src="https://github.com/user-attachments/assets/624613be-e88b-40c3-84f6-8c7d508d20e9" />


## How to download and clone this project
```bash
  git clone https://github.com/24Zack/Fixing-Messed-up-Data-for-Tensile-test-from-the-Bluehill-universal-software-

```

## How to download the pandas library on your terminal
```bash
  pip install pandas

```

# Use of this code

When using the software Bluehill Universal to perform a tensile test in polymers, I had some problems when recording some data because of the systematic error that was made by the machine. 
The error looked like:

![image](https://github.com/user-attachments/assets/e4f29451-2ff4-413f-828f-7f17db55f6b3)

Here, the first column is the time (s), the second colun is the displacement (mm) and the third column is the force (kN).
The error was occuring in the displacement there since the machine was recording an erroned value every now and then.
Therefore, since the data recorded during the tensile test is recorded around 20 thousand times, it is not effective and realistic to manually change every wrong value. That's why I designed the python program there using pandas library to solve that issue.
