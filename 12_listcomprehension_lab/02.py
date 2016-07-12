a_to_z = [chr(n) for n in range(ord('a'),ord('z')+1)]
print [x+y+z for x in a_to_z for y in a_to_z for z in a_to_z]
