// C++ 11
template <typename T> void swap(T& x, T& y) {
  T tmp = std::move(x); // move constructor
  x = std::move(y);     // move assign
  y = std::move(tmp);   // move assign
}
