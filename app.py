from flask import Flask, render_template, request, json

app = Flask(__name__)


users_data = [
    {"name": "Klaus"},
    {"name": "Elijah"},
    {"name": "Nik"},
    {"name": "Freya"},
    {"name": "Marcel"}
]

@app.route('/submit', methods=['POST'])
def submit():
    # Отримуємо дані з форми
    name = request.form['name']

    # Перевіряємо, чи ім'я є в списку
    if any(user['name'] == name for user in users_data):
        # Додаємо нового користувача до списку
        users_data.append({"name": name})

        # Зберігаємо дані у файл JSON
        with open('users.json', 'w') as json_file:
            json.dump(users_data, json_file, indent=2)

        # Повертаємо сторінку
        return render_template('submit.html')
    else:
        # Якщо ім'я не входить до списку, перенаправляємо на головну сторінку
        return redirect (url_for('home'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/page1')
def page1():
    return render_template('page1.html')


@app.route('/page2')
def page2():
    return render_template('page2.html')


@app.route('/page3')
def page3():
    return render_template('page3.html')


@app.route('/library')
def library():
    return render_template('library.html')


@app.route('/page5_1')
def page5_1():
    return render_template('page5_1.html')


@app.route('/page6_1')
def page6_1():
    return render_template('page6_1.html')


@app.route('/page7_1')
def page7_1():
    return render_template('page7_1.html')


@app.route('/page8_1')
def page8_1():
    return render_template('page8_1.html')


@app.route('/page9_1')
def page9_1():
    return render_template('page9_1.html')


@app.route('/page10_1')
def page10_1():
    return render_template('page10_1.html')


@app.route('/page11_1')
def page11_1():
    return render_template('page11_1.html')


@app.route('/page12_1')
def page12_1():
    return render_template('page12_1.html')


@app.route('/page13_1')
def page13_1():
    return render_template('page13_1.html')


@app.route('/page14_1')
def page14_1():
    return render_template('page14_1.html')


@app.route('/page15_1')
def page15_1():
    return render_template('page15_1.html')


@app.route('/page16_1')
def page16_1():
    return render_template('page16_1.html')


@app.route('/page17_1')
def page17_1():
    return render_template('page17_1.html')


@app.route('/page18_1')
def page18_1():
    return render_template('page18_1.html')


@app.route('/page19_1')
def page19_1():
    return render_template('page19_1.html')


@app.route('/page20_1')
def page20_1():
    return render_template('page20_1.html')


@app.route('/page21_1')
def page21_1():
    return render_template('page21_1.html')


@app.route('/page22_1')
def page22_1():
    return render_template('page22_1.html')


@app.route('/page23_1')
def page23_1():
    return render_template('page23_1.html')


@app.route('/page24_1')
def page24_1():
    return render_template('page24_1.html')


@app.route('/page25_1')
def page25_1():
    return render_template('page25_1.html')


@app.route('/page26_1')
def page26_1():
    return render_template('page26_1.html')


@app.route('/page27_1')
def page27_1():
    return render_template('page27_1.html')


@app.route('/page28_1')
def page28_1():
    return render_template('page28_1.html')


@app.route('/page29_1')
def page29_1():
    return render_template('page29_1.html')


@app.route('/page30_1')
def page30_1():
    return render_template('page30_1.html')


@app.route('/page31_1')
def page31_1():
    return render_template('page31_1.html')


@app.route('/page32_1')
def page32_1():
    return render_template('page32_1.html')


@app.route('/page33_1')
def page33_1():
    return render_template('page33_1.html')


@app.route('/page34_1')
def page34_1():
    return render_template('page34_1.html')


@app.route('/page35_1')
def page35_1():
    return render_template('page35_1.html')


@app.route('/page36_1')
def page36_1():
    return render_template('page36_1.html')


@app.route('/page37_1')
def page37_1():
    return render_template('page37_1.html')


@app.route('/page38_1')
def page38_1():
    return render_template('page38_1.html')


@app.route('/page39_1')
def page39_1():
    return render_template('page39_1.html')


@app.route('/page40_1')
def page40_1():
    return render_template('page40_1.html')


@app.route('/page41_1')
def page41_1():
    return render_template('page41_1.html')


@app.route('/page42_1')
def page42_1():
    return render_template('page42_1.html')


@app.route('/page43_1')
def page43_1():
    return render_template('page43_1.html')


@app.route('/page44_1')
def page44_1():
    return render_template('page44_1.html')


@app.route('/page45_1')
def page45_1():
    return render_template('page45_1.html')


@app.route('/page46_1')
def page46_1():
    return render_template('page46_1.html')


@app.route('/page47_1')
def page47_1():
    return render_template('page47_1.html')


@app.route('/page48_1')
def page48_1():
    return render_template('page48_1.html')


@app.route('/page49_1')
def page49_1():
    return render_template('page49_1.html')


@app.route('/page50_1')
def page50_1():
    return render_template('page50_1.html')


@app.route('/page51_1')
def page51_1():
    return render_template('page51_1.html')


@app.route('/page52_1')
def page52_1():
    return render_template('page52_1.html')


@app.route('/page53_1')
def page53_1():
    return render_template('page53_1.html')


@app.route('/page54_1')
def page54_1():
    return render_template('page54_1.html')


@app.route('/page55_1')
def page55_1():
    return render_template('page55_1.html')


@app.route('/page56_1')
def page56_1():
    return render_template('page56_1.html')


@app.route('/page57_1')
def page57_1():
    return render_template('page57_1.html')


@app.route('/page58_1')
def page58_1():
    return render_template('page58_1.html')


@app.route('/page59_1')
def page59_1():
    return render_template('page59_1.html')


@app.route('/page60_1')
def page60_1():
    return render_template('page60_1.html')


@app.route('/page61_1')
def page61_1():
    return render_template('page61_1.html')


@app.route('/page62_1')
def page62_1():
    return render_template('page62_1.html')


@app.route('/page63_1')
def page63_1():
    return render_template('page63_1.html')


@app.route('/page64_1')
def page64_1():
    return render_template('page64_1.html')


@app.route('/page65_1')
def page65_1():
    return render_template('page65_1.html')


@app.route('/page66_1')
def page66_1():
    return render_template('page66_1.html')


@app.route('/page67_1')
def page67_1():
    return render_template('page67_1.html')


@app.route('/page68_1')
def page68_1():
    return render_template('page68_1.html')


@app.route('/page69_1')
def page69_1():
    return render_template('page69_1.html')


@app.route('/page70_1')
def page70_1():
    return render_template('page70_1.html')


@app.route('/page71_1')
def page71_1():
    return render_template('page71_1.html')


@app.route('/page72_1')
def page72_1():
    return render_template('page72_1.html')


@app.route('/page73_1')
def page73_1():
    return render_template('page73_1.html')



@app.route('/page74_1')
def page74_1():
    return render_template('page74_1.html')


@app.route('/page75_1')
def page75_1():
    return render_template('page75_1.html')


@app.route('/back_home_1')
def back_home_1():
    return render_template('back_home_1.html')


@app.route('/agree_1')
def agree_1():
    return render_template('agree_1.html')


@app.route('/clean_and_go_home')
def clean_and_go_home():
    return render_template('clean_and_go_home.html')


@app.route('/page5_2')
def page5_2():
    return render_template('page5_2.html')


@app.route('/page6_2')
def page6_2():
    return render_template('page6_2.html')


@app.route('/page7_2')
def page7_2():
    return render_template('page7_2.html')


@app.route('/page8_2')
def page8_2():
    return render_template('page8_2.html')


@app.route('/page9_2')
def page9_2():
    return render_template('page9_2.html')


@app.route('/page10_2')
def page10_2():
    return render_template('page10_2.html')


@app.route('/page11_2')
def page11_2():
    return render_template('page11_2.html')


@app.route('/page12_2')
def page12_2():
    return render_template('page12_2.html')


@app.route('/page13_2')
def page13_2():
    return render_template('page13_2.html')


@app.route('/page14_2')
def page14_2():
    return render_template('page14_2.html')


@app.route('/page15_2')
def page15_2():
    return render_template('page15_2.html')


@app.route('/page16_2')
def page16_2():
    return render_template('page16_2.html')


@app.route('/page17_2')
def page17_2():
    return render_template('page17_2.html')


@app.route('/page18_2')
def page18_2():
    return render_template('page18_2.html')


@app.route('/page19_2')
def page19_2():
    return render_template('page19_2.html')


@app.route('/come_in')
def come_in():
    return render_template('come_in.html')


@app.route('/go_to_the_cafe')
def go_to_the_cafe():
    return render_template('go_to_the_cafe.html')





if __name__ == '__main__':
    app.run(debug=True)