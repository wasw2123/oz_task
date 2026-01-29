
const form = document.getElementById("form")
if (form){
    form.addEventListener("submit", (e) => {
    e.preventDefault();
    

    const userId = document.getElementById("user_id").value
    const userName = document.getElementById("user_name").value
    const userPhone = document.getElementById("user_phone").value
    const userPw1 = document.getElementById("user_pw").value
    const userPw2 = document.getElementById("user_pw_check").value

    const idTest = /^[a-z0-9]{6,12}$/;
    const pwTest = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/

    if(!idTest.test(userId)){
        alert("아이디는 6~12자 영문 소문자와 숫자여야 합니다.")
        return
    }

    if (!pwTest.test(userPw1)) {
        alert("비밀번호는 영문, 숫자, 특수문자를 포함하여 8자 이상이어야 합니다.")
        return
    } else if (userPw1 !== userPw2) {
        alert("비밀번호가 일치하지 않습니다.")
        return
    }
    
    sessionStorage.setItem("saveId", userId)
    sessionStorage.setItem("saveName", userName)
    sessionStorage.setItem("savephone", userPhone)
    
    location.href = "join_fin.html"
})
}





window.onload = function() {
    const displayId = document.getElementById('id')

    if(displayId){
        const userId = sessionStorage.getItem("saveId")
        const userName = sessionStorage.getItem("saveName")
        const userPhone = sessionStorage.getItem("savephone")

        document.getElementById('id').innerText = `아이디: ${userId}`
        document.getElementById('name').innerText = `이름: ${userName}`
        document.getElementById('phone').innerText = `전화번호: ${userPhone}`
    }
    
}

const back = document.querySelector(".back_btn")
back.addEventListener("click", () => {
    location.href = 'join.html'
})