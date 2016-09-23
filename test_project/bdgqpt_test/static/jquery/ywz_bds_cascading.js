$(function(){
    ///根据所选择的运维站获得变电所
     $('#yunweizhan').change(function(){
       get_biandiansuo('#yunweizhan','#biandiansuo');
       
     })
    });

$(function(){
    ///根据所选择的运维站获得变电所
     $('#id_yunweizhan').change(function(){
       get_biandiansuo('#id_yunweizhan','#id_biandiansuo');
       
     })
    });

$(function(){
        $('#btn_search').click(function(){
       search_data();
        });
});

function search_data(){
    var yunweizhan_id=$('#yunweizhan').val();
    var biandiansuo_id=$('#biandiansuo').val();
    $.ajax(
        {
            type:"POST",
            url:'/search_data/',///?biandiansuo='+biandiansuo,'
            data:{
                biandiansuo_id:biandiansuo_id,
                yunweizhan_id:yunweizhan_id,
            },
            dataType:'json',
            success:function(data)
            /*{
                alert(data)
                var tbody=$('#caozuopiao tbody');
                var tableStr="<tbody>"
                for(var i=0;i<data.length;i++)
                {
                tableStr=tableStr+"<tr>"
                for(var key in data[i])
                {
                   tableStr=tableStr+"<td>"+data[i][key]+"</td>"                  
                }
                tableStr=tableStr+"</tr>"
                }
                tableStr=tableStr+"</tbody>"
                tbody.html("")
                tbody=tbody.html(tableStr)             
                
            }*/
            {
                alert(data)
                $("#div_caozuopiao_table").html(data);
            }
        }
    )
};

///将运维站的值通过ajax方法传给后台，并返回变电所，填充到前台
function get_biandiansuo(yunweizhan,biandiansuo){
    var yunweizhan_id=$(yunweizhan).val();
    alert(yunweizhan_id)
    $.ajax(
    {
    type: "POST",
    url: "/get_biandiansuo/?yunweizhan_id="+yunweizhan_id,
    data:yunweizhan_id,
    dataType:"json",
    success: function(data)
        {
            var opt=$(biandiansuo);
            opt.html('');
            $.each(data, function () 
            {
              opt.append($('<option/>').val(this.id).text(this.value));
            });
        }
    });
};




$(function(){
     $('#startDate').datetimepicker({
      format:'yyyy-mm-dd',
      weekStart:0,
      todayBtn:1,
      autoclose:1,
      todayHighLight:1,
      startView:2,
      maxView:"decade",
      minView:"month",
      forceParse:1,
      showMeridian:0,
      language:'zh-CN',
      pickerPosition: "bottom-left",      
   }).on("changeDate",function(ev){
       $("#endDate").datetimepicker("setStartDate",$("#startDate").val());
   });
});

$(function(){
     $('#endDate').datetimepicker({
      format:'yyyy-mm-dd',
      weekStart:0,
      todayBtn:1,
      autoclose:1,
      todayHighLight:1,
      startView:2,
      maxView:"decade",
      minView:"month",
      forceParse:1,
      showMeridian:0,
      language:'zh-CN',
      pickerPosition: "bottom-left",      
   });
});

  


