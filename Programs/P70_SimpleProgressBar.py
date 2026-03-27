///
def progressBar(count, total):
    percent = (count/total)*100
    bar = '='*int(percent) + '-'
    print(bar)

def show(count, total):
    p = (count/total)*100
    bar = '='*int(p) + '-'
    print(bar)
///
def progressBar(count, total):
    percent = round(100.0 * count / total, 1)
    bar = '='*int(percent) + '-'
    print(bar)

def show(count, total):
    percent = round(100.0 * count / total, 1)
    bar = '='*int(percent) + '-'
    print(bar)
///
