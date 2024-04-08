# phoenix500
remake of Phoenix for ECS Amiga

jotd: reverse-engineering, transcode, graphics conversion
PascalDe73: amiga icons

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