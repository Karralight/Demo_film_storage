#Ứng dụng lưu trữ film

#Định nghĩa Menu hiển thị gợi ý cho người dùng nhập tùy chọn
USER_MENU = """
Nhập
a - Thêm một bộ phim mới
l - Hiển thị danh sách phim
s - Tìm kiếm các bộ phim theo tên
x - Xóa phim theo tên
u - Cập nhật thông tin phim
q - Thoát
Lựa chọn của bạn: """

#Định nghĩa cấu trúc dữ liệu lưu trữ các bộ phim
#list[dict]: mỗi bộ phim là một dictionary nằm trong danh sách
movies = []

#Kiếm tra các bộ phim là duy nhất
prevs = set()

#Định nghĩa các hàm để xử lí
#Thêm một bộ phim mới
def add_movie():
    #Nhập thông tin bộ phim
    name         = input("\nNhập vào tên bộ phim\t: ") #\t: là 1 tab

    while name in prevs:
        print("\nTên phim bị trùng yêu cầu nhập lại!")
        name = input("Xin mời nhập lại tên phim\t: ")

    director     = input("Nhập vào tên đạo diễn\t: ")
    release_year = input("Nhập vào năm phát hành\t: ")

    #Tạo bộ phim
    movie = {
        'name'         : name,
        'director'     : director,
        'release_year' : release_year,  
    }

    #Thêm bộ phim vào danh sách
    movies.append(movie)
    print("\nThêm bộ phim thành công!")
    prevs.add(name)     #Kiểm tra xem nếu tên bị trùng thì yêu cầu nhập lại

#Hiển thị thông tin chi tiết bộ phim:
def show__information_movie(movie):
    movie_name     = movie['name']
    movie_director = movie['director']
    movie_release  = movie['release_year']

    print(f'Tên phim\t: {movie_name}')
    print(f'Tên đạo diễn\t: {movie_director}')
    print(f'Năm phát hành\t: {movie_release}')


#Hiển thị tất cả bộ phimL
def show_list_movie():
    if movies:
        for idx,movie in enumerate(movies, start=1):
            print("\nThông tin bộ phim: ", idx)
            show__information_movie(movie)
    else:
        print("\nDanh sách phim trống")


#Tìm kiếm phim theo tên
def search_movie():
    if movies:
        movie_name = input("\nNhập vào tên bộ phim: ")
        
        for idx,movie in enumerate(movies, start=1):
            if movie_name == movie['name']:
                print("\nThông tin bộ phim tìm kiếm là:", movie_name)
                show__information_movie(movie)
                break
        else:
            print("\nKhông tìm thấy bộ phim nào tên là: ",movie_name)
    else:
        print("\nDanh sách phim trống")


#Xóa phim theo tên:
def remove_movie():
    if movies:
        movie_name = input("\nNhập vào tên: ")

        for idx,movie in enumerate(movies):
            if movie_name == movie['name']:
                del movies[idx]
                print("\nĐã xóa thành công bộ phim tên:",movie_name)
                break
        else:
            print("\nKhông tìm thấy bộ phim nào tên là: ", movie_name)
    else:
        print("\nDanh sách phim trống")


#Cập nhập thông tin phim
def update_movie():
    if movies:
        movie_name = input("\nNhập vào tên bộ phim: ")
        found = [
            idx
            for idx,movie in enumerate(movies)
            if movie['name'] == movie_name
        ]

        if found:
            position = found[0]
            movies[position]['director']   = input("Nhập tên đạo diễn\t: ")
            movies[position]['release_year']    = input("Nhập năm phát hành\t: ")

            print("Cập nhập dữ liệu")
        
        else:
            print("\nKhông có bộ phim tên nào: ", movie_name)
        
    else:
        print("\nDanh sách trống!")


#Nhập sự lựa chọn của người dùng
user_choice = input(USER_MENU)

#Định nghĩa một dict để lưu các option ứng với hành động
options = {
    'a' : add_movie,
    'l' : show_list_movie,
    's' : search_movie,
    'x' : remove_movie,
    'u' : update_movie,
}

#Chọn nhiều option cho đến khi thoát
while user_choice != 'q':
    #Kiểm tra xem tùy chọn có ở bên trong dict không
    #Nếu có giá trị thì gọi hàm để in ra nếu không thì yêu cầu k hợp lệ vui lòng nhập lại
    if user_choice in options:
        option = options[user_choice]
        option()
    else:
        print("\nLựa chọn không hợp lệ, vui lòng nhập lại")
    #Nhập sự lựa chọn của người dùng
    user_choice = input(USER_MENU)
