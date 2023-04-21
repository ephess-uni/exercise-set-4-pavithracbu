""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    Returs the list of lines when a shutdown is initiated
    """
    sd_list = []
    with open(logfile) as log_file:
        for line in log_file:
            if "Shutdown initiated" in line:
                sd_list.append(line.strip())
    return sd_list
    


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    #FILENAME = "data/messages.log"
    print(f"{get_shutdown_events(FILENAME)=}")
