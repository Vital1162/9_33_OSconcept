import random

def print_page(a):
    for n in a:
        print(n,end=" ")
    print()
    
def main():
    # 12 number as well
    page_string =[random.randint(0, 9) for _ in range(12)]
    
    print(f"page referemce string : {page_string}")
    try:
        page_frame = int(input("Enter the page frame here: "))
    except ValueError:
        print(f"Ok you need to type int here")
    
    frame = [-1]*page_frame
    print(f"{len(frame)}")

    
    # FIFO
    fifo_fault = 0
    fifo_order = 0
    turn = 0  
    while turn < 12:
        for i in range(page_frame):
            if page_string[turn] == frame[i]:
                break
            if i == (page_frame - 1):
                fifo_fault += 1
                frame[fifo_order] = page_string[turn]
                fifo_order += 1

        print_page(frame)
        turn += 1

        if fifo_order == page_frame:
            fifo_order = 0

    print("\nFIFO page fault =", fifo_fault, "\n")

    # LRU
    frame_LRU = [-1] * page_frame
    LRU_fault = 0
    turn_LRU = 0 
    write_position = 0 

    while turn_LRU < 12:
        for i in range(page_frame):
            if page_string[turn_LRU] == frame_LRU[i]:
                write_position -= 1
                frame_LRU = frame_LRU[:write_position] + frame_LRU[write_position+1:] + [page_string[turn_LRU]]
                write_position += 1
                break

            if i == (page_frame - 1):
                LRU_fault += 1
                if write_position != page_frame:
                    frame_LRU[write_position] = page_string[turn_LRU]
                    write_position += 1
                else:
                    frame_LRU = frame_LRU[1:] + [page_string[turn_LRU]]

        print_page(frame_LRU)
        turn_LRU += 1

    print("\nLRU page fault =", LRU_fault)
    
if __name__ == "__main__":
    main()