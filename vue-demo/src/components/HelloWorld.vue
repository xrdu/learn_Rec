<template>
<el-table :data="tableData" style="width: 100%">
      <el-table-column
        prop="id"
        label="id"
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="姓名"
        width="180">
      </el-table-column>
      <el-table-column
        prop="gender"
        label="性别">
      </el-table-column>
      <el-table-column
        prop="grade"
        label="年级">
      </el-table-column>
      <el-table-column
        prop="major"
        label="专业">
      </el-table-column>
      <el-table-column
        prop="class"
        label="班级">
      </el-table-column>
      <el-table-column
        prop="academy"
        label="学院">
      </el-table-column>
      <el-table-column
        prop="school"
        label="学校">
      </el-table-column>
      <el-table-column
        prop="avgTestScore"
        label="平均分">
      </el-table-column>
</el-table>
</template>

<script>
import axios from 'axios'
  export default {
    methods: {
      handleClick(row) {
        console.log(row);
      },
      getData(){
        /*将路径更改为后端运行的服务器地址+（蓝图名）+视图函数路由*/
        const path = 'http://127.0.0.1:5000/'
        axios({
          url: path,
          method: 'get'//还有get方法
          //data：{post的时候需要传递条件}
        }).then((res) => {
          console.log(res.data)
          this.tableData = res.data
          //填写接收res的函数或变量名
        }).catch((error) => {
          console.error(error);
      });
      }
    },
    data() {
      return {
        tableData: [],
      }
    },
    created() {
        this.getData();
    },
  }
</script>