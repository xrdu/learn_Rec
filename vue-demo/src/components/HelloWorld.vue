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
        prop="username"
        label="性别">
      </el-table-column>
      <el-table-column
        prop="email"
        label="年级">
      </el-table-column>
      <el-table-column
        prop="phone"
        label="专业">
      </el-table-column>
      <el-table-column
        prop="website"
        label="班级">
      </el-table-column>
      <el-table-column
        prop="address.street"
        label="学院">
      </el-table-column>
      <el-table-column
        prop="company.name"
        label="学校">
      </el-table-column>
</el-table>
</template>

<script>
import axios from 'axios'
  export default {
    methods: {
      handleClick(row) {
        console.log(row);
      }
    },
    data() {
      return {
        tableData: []
      }
    },
    created() {
		/*将路径更改为后端运行的服务器地址+（蓝图名）+视图函数路由*/
        const path = 'http://jsonplaceholder.typicode.com/users';
        axios({
          url: path,
          method: 'get'//还有get方法
          //data：{post的时候需要传递条件}
        }).then((res) => {
          //console.log(res.data)
          this.tableData = res.data
          //填写接收res的函数或变量名
        }).catch((error) => {
          console.error(error);
      });
    },
  }
</script>