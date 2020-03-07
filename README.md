# Egyptians and Bitwise Operations

I thought I'd upload something interesting as my first repo, so that I can entertain and, hopefully, edify whilst I work out exactly what I'm doing with GitHub.

## Russian Peasant Multiplication

### The History

Allegedly, before calculators were invented, people still needed to multiply. The Ancient Egyptians, along with many other ancient civilisations, used multiplication tables, which can be imaged as akin to today's elementary / primary school children's times tables, except more comprehensive. Back then, as it is now, multiplying two water lillies to get a Heh was a challenge.

( Source: https://en.wikipedia.org/wiki/Egyptian_numerals )

In any case, in order to be able to multiply without using tables, a system was needed to get the correct result but without any complex arithmetic. Hence, Ancient Egyptian multiplication was born. I, however, know it as Russian Peasant Multiplication, hence the title of this section of the README, peasant.py, and the homonymous function therein.

( Source: https://en.wikipedia.org/wiki/Ancient_Egyptian_multiplication )

### The Mathematics

So what the Ancient Egyptians came up with is actually pretty neat. The other name for this method of multiplication is mediation and duplation, where the words, in this context, mean halving and doubling.

( Yes, the word mediation's other meaning is etymologically related.

Source: https://www.etymonline.com/word/mediation )

Take two numbers - say, 5 and 2. Picture an area, quadrangular in nature, with sides of length 5 and 2. The area is, of course, 10. Now double 5 and halve 2 - 10 and 1. If we calculate the area as before, we once again get 10. This works because instead of putting two blocks of 1x5 together, we've got one long block of 1x10. Ok, but what happens if we have to halve an odd number? How about 5 and 3?

Well, odd numbers are halved then **rounded down**. To quickly run through it, 5x3 becomes 10x1 and we get 10 again as our answer. Hmmm. We're short, and it's pretty obvious why. When we rounded the three down, we lost out on 0.5x10. Well, it just so happens that 0.5x10 - or 5 -  is the number that preceded 10 in the duplication process! Essentially, every time an odd number comes up as the mediator, make a note of the duplicator, and add it on to the final value at the end. To refer back to our area analogy, think of it as one block of 1x10 and one of 1x5.

I'll go through a longer example, then explain my code.

123 x 123 ... *odd number*, let's make a note of the duplicator: 123

246 x 61 ... *odd number*, let's make a note of the duplicator: 246

492 x 30

984 x 15 ... *odd number*, let's make a note of the duplicator: 984

1968 x 7... *odd number*, let's make a note of the duplicator: 1968

3936 x 3 ... *odd number*, let's make a note of the duplicator: 3936

7872 x 1 ... add to this the sum of the duplicators ... 123 + 246 + 984 + 1968 + 3936 = 7257



7257 + 7872 = 123 x 123 = 15129




( A far better explanation: http://mathforum.org/dr.math/faq/faq.peasant.html )

Okay, so maybe this isn't the most efficient way to multiply...

Unless I had some kind of machine for which this would be child's play...

### The Code Explained

Realistically, the reason I wrote peasant.py is that I wanted to use bitwise operators. They're cool, and I don't really see them used all too frequently, which is a shame.

The ret_val is the variable we shall be returning. Whilst b, the mediator, is greater than zero, we will be running the loop. The first bit of code which is interesting is the following line:

```
if b & 1:
```

The ampersand is the bitwise and operator, and it is checking if b is even or odd. The ampersand, compares the binary representations of two equal length binary representations, and multiplies them. Not being equal, the operator takes as much as it can - 1 digit, in this case. The final digit of 1 is 1, which also happens to be the same as the final digit of any other odd number. Hence, if the number is odd we get 1x1, whereas we get 1x0 if the number is even. The if coniditional usually takes a boolean value, but as it interprets integers other than zero as True and zero as False, it works out perfectly for us, only adding on to the ret_val if b is odd (and so it shares a final digit (in binary) with 1).

Next, the following may also be unfamiliar:

```
a <<= 1
b >>= 1
```

Those signs are akin to the += or -= operators. They could be expanded in much the same way. What they do is shift the bits either left or right one place, depending on the direction of the arrows. In binary, this, of course, serves to double or halve the numbers. A zero is added as the final digit of the rightward shifted number.

And that's pretty much it! Unlike in the example we did, when it hits 1 with the mediator, this function adds it on to retval as well, allowing us to simply:

```
return ret_val
```

### Unittests

It's unittested. If you're too lazy to navigate to the folder and run the tests through the command line, there's a test_lazily.zsh file... I'm not judging, I'm that kind of person too...

Thanks for reading if you got through all that!