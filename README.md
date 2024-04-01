# phoenix500
remake of Phoenix for Amiga

todo:

reverse functions of jump_table_040E
jump table? 0EE5
0EA4: deactivate bird in table?
then what does it do?
; pops stack and jumps
; occurs when bird enemy is shot        
0EE3: E1              POP     HL                  
0EE4: E1              POP     HL                  
0EE5: E9              JP      (HL) 
