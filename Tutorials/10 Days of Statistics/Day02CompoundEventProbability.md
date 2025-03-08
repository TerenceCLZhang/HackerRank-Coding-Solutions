**Question**

There are 3 urns labeled X, Y, and Z

- Urn X contains 4 red balls and 3 black balls
- Urn Y contains 5 red balls and 4 black balls
- Urn Z contains 4 red balls and 4 black balls

One ball is drawn from each of the 3 urns. What is the probability that, of the 3 balls drawn, 2 are red and 1 black?

1. 10 / 63
2. 2 / 7
3. 17 / 42 <-- **ANSWER**
4. 31 / 126

**Explanation**

Each urn has a certain probability of drawing a red or black ball:

- Urn X: P(Rx) = 4 / 7 and P(Bx) = 3 / 7
- Urn Y: P(Ry) = 5 / 9 and P(By) = 4 / 9
- Urn Z: P(Rz) = 4 / 8 and P(Bz) = 1 / 2

We need to consier three possible possibilities:

- Red from X, Red from Y, and Black from Z: P(Rx) x P(Ry) x P(Bz) = 4 / 7 x 5 / 9 x 1 / 2 = 20 / 126
- Red from X, black from Y, and Red from Z: P(Rx) x P(By) x P(Rz) = 4 / 7 x 4 / 9 x 1 / 2 = 16 / 126
- Black from X, Red from Y, and Red from Z: P(Bx) x P(Ry) x P(Rz) = 3 / 7 x 5 / 9 x 1 / 2 = 15 / 126

Adding up all the possibilities:

20 / 126 + 16 / 126 + 15 / 126 = **17 / 42**.
