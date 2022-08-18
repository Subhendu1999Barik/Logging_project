import logging
logging.basicConfig(filename="test1.log",level=logging.WARNING ,format='%(levelname)s %(asctime)s %(name)s %(message)s')

def devide(a,b) :
    logging.info("the number enter by the user is %s and %s ",a,b)
    try:
        logging.info("we are into the function")
        div = a/b
        logging.info("we completed the division operation")
        logging.info("result of the code is %s",div)
        return div
    except Exception as e:
        logging.exception(e)

devide(3,0)