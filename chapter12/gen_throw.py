def gen_func():
    #1. 可以产出值 2. 可以接收值
    try:
        yield "http://www.baidu.com"
    except Exception as _:
        pass
    yield 2
    yield 3
    return "zhaoguom"

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception, "download error")
    print(next(gen))
    gen.throw(Exception, "download error")
