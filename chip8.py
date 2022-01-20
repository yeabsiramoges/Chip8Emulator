#input
self.key_inputs = [0]*16 #storing key input states from a 16 button keyboard

#output
self.display_buffer = [0]*32*64 #outputs to a 64x32 display, an array of pixels

#memory
self.memory = [0]*4096 #chip8 interperters have a memory of 4096 bytes, including the interpeter itself, the fonts, and where the program os supposed to run
