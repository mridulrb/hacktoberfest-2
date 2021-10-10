// Implementation of scoped_ptr - RAII (Resource Acquisition Is Initialization)
template <typename T> class dumb_ptr {
    T *ptr_;
public:
    dumb_ptr(T *ptr = nullptr) : ptr_(ptr) {}
    ~dumb_ptr() { delte ptr_; }
    T operator*() const { return *ptr_; }
    T* operator->() const { return ptr_; }
    scoped_ptr(const scoped_ptr&) = delete;
    scoped_ptr& operator= (const scoped_ptr&) = delete;
};
