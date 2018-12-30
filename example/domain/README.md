
# Domain 样例

此样子仅供参考，只为更方便的为大家讲解entanmo dapp的使用。

**注：假设大家都会发布dapp，如果大家还不会请查看前面章节**

### 1.配置及路由 
**我们从哪里开始呢？**

代码都会有一个开始位置，比如java中`main()`函数, Android中 `onCreate()`等等。在entanmo中合约的入口文件是[ `init.js`](./init.js)

	module.exports = async function () {
		//...
		
		//这里是注册了两个合约接口，接口需要1000，1001
	  	app.registerContract(1000, 'domain.register')
	  	app.registerContract(1001, 'domain.set_ip')

  		//....
	}

很显然，可以看到两个注册的接口（并不是合约）。


然后可以查看interface目录下的[domain.js](./interface/domain.js) ,这里定义了路由访问规则。

	app.route.get('/domain/:address',  async function (req) {
	  let result = await app.model.Domain.findOne({
	      condition: { address: req.params.address }
	  })
	  return result
	})
	
	//....
访问规则是:  xxx:xxx/xxx/domain/myAddress 为什么要这么写，其实前面是dapp路径，这里可以跟大家明确下，entanmo中的dapp访问都是 `ip:port/dappid/router`,dappid其实就是注册dapp返回的合约唯一标识符。
那么此处我们该如何访问呢？
	
	//这样就可以访问到这个合约接口
	http://ip:port/dappid/domain/:address
	
其实如果大家只是为了测试，可以直接查看[helloworld.js](./interface/helloworld.js)

	app.route.get('/helloworld',  async function (req) {
	  return { message: 'helloworld' }
	})	
	//...

大家可以看到此接口是没有合约序号对应的（就是init.js中没有注册接口）,这是由于此接口只是返回状态，不做任何合约内部操作。
	
	//访问方式
	http://ip:port/dappid/helloworld
	//返回helloworld
	

### 2.模型定义
模型的定义其实是定义数据结构，让数据以什么方式存储到区块链上，在dapp模版中，我们可以看到model目录，此example对应的[domain.js](./model/domain.js)就是对于的数据模型定义文件。

	module.exports = {
	  name: 'domains',
	  fields: [
	    {
	      name: 'address',
	      type: 'String',
	      length: 256,
	      not_null: true,
	      index: true
	    },
	    {
	      name: 'ip',
	      type: 'String',
	      length: 15
	    },
	    {
	      name: 'owner',
	      type: 'String',
	      length: 50,
	      not_null: true,
	    },
	    {
	      name: 'suffix',
	      type: 'String',
	      length: 10,
	      not_null: true,
	      index: true
	    }
	  ]
	}
	
可以发现，定义了一张domain表，里面包含，address，ip，owner 等等，下一小节，我们将讲到合约中如何使用。

### 3.合约实现
之前我们已经说过，entanmo官方为了让开发者更容易的开发合约，在设计上就是尽量让开发者只做逻辑相关的工作。那我们来看一下contract目录下的[domain.js](./contract/domain.js)实现

	module.exports = {
		register: async function(address) {
	  		//锁定当前地址操作数据库
	    	app.sdb.lock('domain.register@' + address)
	    	//查询此地址是否注册过
	    	let exists = await app.model.Domain.exists({address: address})
	    	if (exists) return 'Address already registered'
	    	//如果没有注册，直接create一条数据
	    	app.sdb.create('Domain', {
	      	address: address,
	      	owner: this.trs.senderId,
	      	suffix: address.split('.').pop()
	    	})
	  	},
	  	set_ip: async function(address, ip) {
	    	app.sdb.lock('domain.register@' + address)
	    	let exists = await app.model.Domain.exists({address: address})
	    	if (!exists) return 'Address not exists' 
	    	app.sdb.update('Domain', { ip: ip }, { address: address })
	  	}
	}

其实很简单，注释中已经说明，是不是很简单。其实开发者只需要关注合约中的逻辑实现即可。
	
然后重启应用节点即可，咱们dapp就成功发布啦，就这么简单。