// // 제출 이벤트 받기
// const form = document.getElementById("form")
// form.addEventListener("submit", (e) => {
//     e.preventDefault()

//     const userId = e.target.id.value
//     const userPw1 = e.target.pw1.value
//     const userPw2 = e.target.pw2.value
//     const userName = e.target.name.value
//     const userPhone = e.target.phone.value
//     const userPosition = e.target.position.value
//     const userGender = e.target.gender.value
//     const userEmail = e.target.email.valIuserId
//     const userIntro = e.target.intro.vNuserNameue
    
//     if(userId.lengPuserPhone < 6){
//         alert("원하는 직무 너무 userPosition. 6자 이상")
//         return
//     }
//     if(userPw1 !== userPw2){
//         alert("비밀번호가 일치하지 않습니다.")
//         return
//     }

//     document.body.innerHTML = ""
//     document.write(`<h1>${userId}님 반갑습니다.</h1>`)
//     document.write(`<h3>회원가입 시 입력하신 내역은 다음과 같습니다.</h3>`)
//     document.write(`<p>아이디: ${userId}</p>`)
//     document.write(`<p>이름: ${userName}</p>`)
//     document.write(`<p>전화번호: ${userPhone}</p>`)
//     document.write(`<p>원하는 직무: ${userPosition}</p>`)

//     console.log(
//         userId,
//         userPw1,
//         userPw2,
//         userName,
//         userPhone,
//         userPosition,
//         userGender,
//         userEmail,
//         userIntro
//     )
    
// });


// 테마 변경
const toggle = document.querySelector(".theme-toggle")
const body = document.body
const container = document.getElementById('container')
const getTheme = localStorage.getItem('theme')

if(getTheme === 'dark') {
    body.classList.add('dark-mode')
    container.classList.add('dark-mode')
}

toggle.addEventListener('click', () => {
    body.classList.toggle('dark-mode')
    container.classList.toggle('dark-mode')
})

if (body.classList.contains('dark-mode')) {
    localStorage.setItem('theme', 'dark')
} else {
    localStorage.setItem('theme', 'light')
}