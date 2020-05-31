
import speedtest

# Functions


def testSpeed() -> dict:
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()
    return s.results.dict()


def printDict(dict):
    for key in dict:
        print(key, ": ", dict[key])
