"""
Persistent connections

    Persistent connections avoid the overhead of re-establishing a connection to the database in each request.
    They’re controlled by the CONN_MAX_AGE parameter which defines the maximum lifetime of a connection.
    It can be set independently for each database.

    The default value is 0, preserving the historical behavior of closing the database connection at the end of
    each request. To enable persistent connections, set CONN_MAX_AGE to a positive number of seconds.
    For unlimited persistent connections, set it to None.

Caveats

    Since each thread maintains its own connection, your database must support at least
    as many simultaneous connections as you have worker threads.

    The development server creates a new thread for each request it handles,
    negating the effect of persistent connections. Don’t enable them during development.

When and how many threads are created? This depends on the server used:
    [1] runserver (the development server) starts a new thread for every request;
    [2] gunicorn reuses threads across requests;
"""
"""
[CONN_MAX_AGE: 0][runserver]
[每个request都要创建新线程，每个线程创建单独连接]

[CONN_MAX_AGE: 0][gunicorn]
[request被分配到gunicorn的4个worker进程，每个worker进程内的线程可以被request重用，每个request创建单独连接]

[CONN_MAX_AGE: None][runserver]
[每个request都要创建新线程，每个线程创建单独连接]

[CONN_MAX_AGE: None][gunicorn]
[request被分配到gunicorn的4个worker进程，每个worker进程内的线程可以被request重用，每个worker进程内的线程创建的连接可以被request重用]
"""
