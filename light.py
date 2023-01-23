from PDFOps import PDFOps

p = PDFOps()

print('merge [in1.pdf,in2.pdf,...] [out.pdf]\ncompress [in1.pdf,in2.pdf,...] [out1.pdf,out2.pdf,...]\nfix_rotation [in1.pdf,in2.pdf,...] [out1.pdf,out2.pdf,...] [type]')
cmd = input().split(' ')

if cmd[0] == 'merge':
    p.simple_merge(cmd[1].split(','), cmd[2])
elif cmd[0] == 'compress':
    p.compress(cmd[1].split(','), cmd[2])
elif cmd[0] == 'fix_rotation':
    type = 0 if cmd[3] == 'p' else 90
    p.fix_rotation(cmd[1].split(','), cmd[2].split(','), type)