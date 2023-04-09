    document.addEventListener('DOMContentLoaded',function(){
          setTimeout(() => {
            document.getElementById('message').style.display='none';
          }, 2000);

    document.getElementById('file').addEventListener('change', function(){
            document.getElementById('form').submit()
        }
    )
});