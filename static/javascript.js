var answer;
var question_n = 1; // 문제 번호
var answer_n = 0; // 맞춘 개수



// 정답 가져오고 힌트 세팅하기
function get_answer(){
    $.ajax({
        type: "GET",
        url: "/answer"

    })
    .done(function(result){
        // hint 안에 값 넣기
        document.getElementById("hint").innerHTML = ""
        
        for (i in result.hint){
            var lyrics_content = document.createTextNode(result.hint[i]);
            const lyrics_div = document.createElement('div')
            lyrics_div.appendChild(lyrics_content)
            document.getElementById("hint").appendChild(lyrics_div);
        }
        
        

        
        // answer 값 세팅
        answer = result.answer;
    })
}


// 페이지 로드 시 작동
$(function() {
    $(document).ready(
        get_answer()
        
    )
    document.getElementById("answer_n").innerHTML = answer_n.toString();
    document.getElementById("question_n").innerHTML = question_n.toString();
})



$(function() {   // <input>요소에 문자가 입력될 때마다 호출됨.

    $("#name").keyup(function() {

        $.ajax({ // Ajax 요청을 작성하고 GET 방식으로 전송함.

        url: "/search",
        type: "GET",
        data: { keyword : $(this).val() }   

        })       // Ajax 응답을 정상적으로 받으면 실행됨.

        .done(function(result) {
            const recommendBox = document.querySelector("#suggestion_box");
            recommendBox.classList.remove('invisible');

            recommendBox.innerHTML = "";

            const suggestedItems = document.createElement('div')
            suggestedItems.id = "suggested-items"
            
            recommendBox.appendChild(suggestedItems);

            // item별로 split하기
            var items = result.split('\n');

            // for문 돌면서 item 추가
            for (var i in items) {
            
            var song_name = document.createTextNode(items[i]);
            var suggestedItem = document.createElement('div')
            suggestedItem.className = "item"

            suggestedItem.addEventListener('click', function(e){
                document.getElementById("name").value = this.textContent;
            });

            suggestedItem.appendChild(song_name);
            suggestedItems.appendChild(suggestedItem);
            }
        })
    })
})


// 재시작
$(function() { 
        $('#restart-button').click(function(){
        
        get_answer();
  
        question_n = 1;
        answer_n = 0;

        document.getElementById("answer_n").innerHTML = answer_n.toString();
        document.getElementById("question_n").innerHTML = question_n.toString();

        alert("퀴즈를 재시작합니다!");
    }) 
}) 


//정답 제출
$(function() {
    $('#submit-button').click(function(){
        var song_name = $('#name').val();

        // 제출 값과 정답이 같으면, 정답 처리 후 다음 문제로

        if (answer === song_name) {
            alert("정답입니다!");
            answer_n += 1;
            get_answer();
            question_n += 1;
            if (question_n > 10){
                alert("10개 중 "+answer_n+"개를 맞추셨습니다!")
                question_n = 1;
                answer_n = 0;
            }
            
            document.getElementById("answer_n").innerHTML = answer_n.toString();
            document.getElementById("question_n").innerHTML = question_n.toString();

        }else{
            alert("오답입니다ㅠ");
            get_answer();
            question_n += 1;
            if (question_n > 10){
                alert("10개 중 "+answer_n+"개를 맞추셨습니다!")
                question_n = 1;
                answer_n = 0;
            }
            document.getElementById("question_n").innerHTML = question_n.toString();
        }
    })
}) 
