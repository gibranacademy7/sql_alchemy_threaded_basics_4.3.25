# Main Thread
# │
# ├───► Start Thread A ────► [Function: print_various_things("A")]
# │                               │
# │                               │  1.Print numbers
# │                               │  2.Print quotes
# │                               │  3.Print space facts
# │                               │  4. ** (Lock Acquired) Print Capital Cities **
# │                               │  5.Print programming languages
# │                               │
# │                               └──► Thread A completes
# │
# ├───► Start Thread B ────► [Function: print_various_things("B")]
# │                               │
# │                               │  1.Print numbers
# │                               │  2.Print quotes
# │                               │  3.Print space facts
# │                               │  4. ** (Lock Acquired) Print Capital Cities **
# │                               │  5.Print programming languages
# │                               │
# │                               └──► Thread B completes
# │
# └──► Print
# "Both threads have completed execution."
