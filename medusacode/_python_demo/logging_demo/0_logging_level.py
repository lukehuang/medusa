"""
logging.debug(msg[, *args[, **kwargs]])
    Logs a message with level DEBUG on the root logger.
    The msg is the message format string,
    and the args are the arguments which are merged into msg using the string formatting operator.
    (Note that this means that you can use keywords in the format string, together with a single dictionary argument.)

    There are two keyword arguments in kwargs which are inspected:
        exc_info:
            if it does not evaluate as false, causes exception information to be added to the logging message.
            If an exception tuple (in the format returned by sys.exc_info()) is provided, it is used;
            otherwise, sys.exc_info() is called to get the exception information.
        extra:
            The other optional keyword argument is extra which can be used to pass a dictionary
            which is used to populate the __dict__ of the LogRecord created for the logging event with user-defined attributes.
            These custom attributes can then be used as you like.
            For example, they could be incorporated into logged messages.

logging.info(msg[, *args[, **kwargs]])
    Logs a message with level INFO on the root logger. The arguments are interpreted as for debug().

logging.warning(msg[, *args[, **kwargs]])
    Logs a message with level WARNING on the root logger. The arguments are interpreted as for debug().

logging.error(msg[, *args[, **kwargs]])
    Logs a message with level ERROR on the root logger. The arguments are interpreted as for debug().

logging.critical(msg[, *args[, **kwargs]])
    Logs a message with level CRITICAL on the root logger. The arguments are interpreted as for debug().

logging.exception(msg[, *args[, **kwargs]])
    Logs a message with level ERROR on the root logger. The arguments are interpreted as for debug(),
    except that any passed exc_info is not inspected.
    Exception info is always added to the logging message.
    This function should only be called from an exception handler.
"""
