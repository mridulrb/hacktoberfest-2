// C, only for int's
int sum_all(int nargs, ...) {
    va_list ap;
    int cnt = 0;
    va_start(ap, nargs);
    for (int i = 0; i < nargs; ++i)
        cnt += va_arg(ap, int);
    va_end(ap);
    return cnt;
}

// C++ 17
template <typename ... T>
auto sum_all_new (T ... args) { 
    return (args + ...); 
}
