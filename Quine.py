# 23rd July 2020
# Manas Dash
# Quine : Computational Self replication
# A quine is a computer program which takes no input and
# produces a copy of its own source code as its only output.
# https://en.wikipedia.org/wiki/Quine_(computing)

s = 's=%r;print(s%%s)';print(s%s)

# output
# s='s=%r;print(s%%s)';print(s%s)

# What is a intron then?

# intron
t='';s='t=input()or t;print(f"t={repr(t)};s={repr(s)};exec(s)#{t}")';exec(s)

# output
# hello (input)
# t='hello';s='t=input()or t;print(f"t={repr(t)};s={repr(s)};exec(s)#{t}")';exec(s)#hello

# execute the output again and see what happend