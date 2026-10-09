# Codenova-task-1-Password-generator
Built a lightweight, cryptographically secure password generator in Python here I use 
​Cryptographic security uses Python’s secrets module to leverage OS-level CSPRNG for true unpredictability.
​Guaranteed complexity for Expliciting seeds one letter, one number, and one symbol into the pool so you never accidentally generate a weak password.
​Pattern breaking for Scrambles the list using secrets.SystemRandom().shuffle() so the mandatory characters never sit in a predictable sequence.