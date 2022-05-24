     # Check for INT_MAX to avoid overflow and see if
        # result can minimized
        if (sub_res != sys.maxsize and sub_res + 1 < res):
            res