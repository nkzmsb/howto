import setting

set_dic = setting.setting()

if set_dic["MODE"] == "WhereFrom":
    def main():
        import logging

        import module1, module2

        logging.basicConfig(level=logging.DEBUG)
        
        module1.f1()
        module1.f2()
        module2.f1()
        module2.f2()

        if False:
            logging.debug("debug log!!")

else:
    def main():
        pass



if __name__ == "__main__":
    main()