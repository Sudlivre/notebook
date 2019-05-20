// not true

var data = { "g1": [1, 2, 3], "g2": [4, 5, 6], "name": ["g1", "g2"] };


var data_list = [];
for (i = 0; i < data.name.length; i++) {
    var new_name = data.name[i]
    var obj_data = [];
    var ser_obj = {
        "name": new_name,
        "group": "test",
    };
    var t_name = ser_obj.name
    ser_obj["data"] = data.t_name
    data_list.push(ser_obj);
};
console.log(data_list);
