a = 5
print(a, " = ", bin(a))
b = 6
print(b, " = ", bin(b))

print("%d & %d = %d (%s)" % (a, b, a & b, bin(a & b)))
print("%d | %d = %d (%s)" % (a, b, a | b, bin(a | b)))
print("%d ^ %d = %d (%s)" % (a, b, a ^ b, bin(a ^ b)))
print("%d << 1 = %d (%s)" % (a, a << 1, bin(a << 1)))
print("%d >> 1 = %d (%s)" % (a, a >> 1, bin(a >> 1)))