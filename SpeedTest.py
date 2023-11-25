import SpeedTest

def check_speed():

    st = SpeedTest.SpeedTest()
    st.get_best_server() 
    # find the best server for testing
    download_speed = st.download() / 10**6
    # convert to mbps
    upload_speed = st.upload() / 10**6  

    