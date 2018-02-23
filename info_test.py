import systeminfo 
def main():
    output = systeminfo.get_platform_info()
    print(output)
    return output
