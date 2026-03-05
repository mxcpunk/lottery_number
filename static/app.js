// 处理“获取组合信息”按钮点击
document.getElementById("get_totals").addEventListener("click", function() {
    fetch('/get_totals')
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            document.getElementById("status0").value = data.total_0;
            document.getElementById("status1").value = data.total_1;
            document.getElementById("total").value = data.total;
        })
        .catch(error => {
            console.error("Error fetching totals:", error);
        });
});

// 处理“查询Status”按钮点击
document.getElementById("check_status").addEventListener("click", function() {
    const numbers = [
        document.getElementById("num1").value,
        document.getElementById("num2").value,
        document.getElementById("num3").value,
        document.getElementById("num4").value,
        document.getElementById("num5").value,
        document.getElementById("num6").value,
        document.getElementById("num7").value
    ];

    fetch('/check_status', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ numbers: numbers })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json();
    })
    .then(data => {
        document.getElementById("status_result").innerText = `Status: ${data.status}`;
    })
    .catch(error => {
        console.error("Error checking status:", error);
    });
});

// 处理“清除”按钮点击
document.getElementById("clear_inputs").addEventListener("click", function() {
    const fields = ["num1", "num2", "num3", "num4", "num5", "num6", "num7"];
    fields.forEach(field => {
        document.getElementById(field).value = '';
    });
    document.getElementById("status_result").innerText = '';
});
