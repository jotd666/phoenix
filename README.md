# phoenix500
remake of Phoenix for Amiga

todo:

reverse functions of jump_table_040E
jump table? 0EE5
check ,d6 shit
check BC,\$0.0.
check DE,\$0.0.
debug copy_bank

converter: ADD     $DE] => add 0xA1 !!!!

detect: | [$3960: LD      A,L]
        | [$3961: ADD     $05]
        | [$3963: LD      L,A]