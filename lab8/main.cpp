#include <iostream>
#include <vector>

template <typename T>
class Matrix {
private:
    uint8_t mRows;
    uint8_t mCols;

    std::vector<T> data;

public:
    Matrix() : mRows(0), mCols(0) {}
    explicit Matrix(uint8_t dimension) : mRows(dimension), mCols(dimension), data(dimension * dimension) {}
    Matrix(uint8_t rows, uint8_t cols) : mRows(rows), mCols(cols), data(rows * cols) {}

    void validateIndexes(size_t row, size_t col) const {
        if (row < 0 or row >= mRows)
            throw std::overflow_error("Invalid row index");
        if (col < 0 or col >= mCols)
            throw std::overflow_error("Invalid column index");
    }

    Matrix operator+(T value) {
        Matrix result(this->mRows, this->mCols);

        for (size_t i = 0; i < this->mRows; i++) {
            for (size_t j = 0; j < this->mCols; j++) {
                result(i, j) = this(i, j) + value;
            }
        }

        return result;
    }

    Matrix operator+(const Matrix &b) {
        if (mRows != b.mRows || mCols != b.mCols)
            throw std::overflow_error("Cannot add these matrices");

        Matrix result(mRows, mCols);

        for (size_t i = 0; i < mRows; i++) {
            for (size_t j = 0; j < mCols; j++) {
                result(i, j) = operator()(i, j) + b(i, j);
            }
        }

        return result;
    }

    friend Matrix operator*(const Matrix &m, double value) {
        Matrix result(m.mRows, m.mCols);

        for (size_t i = 0; i < m.mRows; i++) {
            for (size_t j = 0; j < m.mCols; j++) {
                result(i, j) = m(i, j) * value;
            }
        }

        return result;
    }

    Matrix operator*(const Matrix &b) {
        if (mCols != b.mRows)
            throw std::overflow_error("Cannot add these matrices");

        auto result = Matrix<T>(mRows, b.mCols);

        for (size_t i = 0; i < result.mRows; i++) {
            for (size_t k = 0; k < mCols; k++) {
                double tmp = operator()(i, k);
                for (size_t j = 0; j < result.mCols; j++) {
                    result(i, j) += tmp * b.operator()(k, j);
                }
            }
        }

        return result;
    }

    void fill(T value) {
        for (size_t i = 0; i < this->mRows; i++) {
            for (size_t j = 0; j < this->mCols; j++) {
                data[i * mCols + j] = value;
            }
        }
    }

    Matrix transpose() {
        Matrix result(mCols, mRows);

        for (size_t i = 0; i < mRows; i++) {
            for (size_t j = 0; j < mCols; j++) {
                result(j, i) = operator()(i, j);
            }
        }

        return result;
    }

    T &operator()(size_t i, size_t j) {
        validateIndexes(i, j);
        return data[i * mCols + j];
    }

    const T &operator()(size_t i, size_t j) const {
        validateIndexes(i, j);
        return data[i * mCols + j];
    }

    void print() {
        for (int i = 0; i < this->mRows; i++) {
            for (int j = 0; j < this->mCols; j++) {
                std::cout << std::left << "\t" << this->operator()(i, j);
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    auto dat = Matrix<float>(3);

    std::cout << "empty" << std::endl;
    dat.print();

    std::cout << "filled" << std::endl;
    dat.fill(10);
    dat.print();

    std::cout << "mul" << std::endl;
    auto second = Matrix<float>(3);
    second(1, 0) = 3;
    dat = dat * second;
    dat.print();

    std::cout << "transpose" << std::endl;
    auto h = Matrix<float>(3);
    h(1, 0) = 3;
    h.print();

    std::cout << std::endl;

    auto trans = h.transpose();
    trans.print();

    return 0;
}

