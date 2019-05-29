package scala.ca.uwaterloo.conf

class WebConf(args: Seq[String]) extends Conf(args) {

  mainOptions = Seq(term, field, solr, index)

  val solr = opt[String](descr = "Solr base URLs", required = true)

  val index = opt[String](descr = "Solr index name", default = Some("cw09b-url"), required = true)
  val field = opt[String](descr = "search field", required = true)

  val rows = opt[Int](descr = "number of rows to return per request", default = Some(1000))
  val parallelism = opt[Int](descr = "number of cores/executors/etc. to use", default = Some(9 * 16))

  val output = opt[String](descr = "output file path", required = true)

  codependent(field, term, solr, index)

  verify()

}