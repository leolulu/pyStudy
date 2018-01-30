def main():

    def test(who):
        def test_in(eat):
            print(who+eat)
        return test_in

    result = test("我")
    result("汉堡")


if __name__ == "__main__":
    main()
